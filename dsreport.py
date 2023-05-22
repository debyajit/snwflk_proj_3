
# Package
import xml.etree.ElementTree as ET
import pandas as pd
import re

# DB Record finding
def Record_extract(job, src):
    Out_rcrd = []
    In_rcrd = []

    # Job  Property = OutputPins Record
    for r in job.findall(".//Property[@Name='OutputPins']/.."):
        # Record { Property StageType = src
        for p in r.findall(".//Property[@Name='StageType']"):
            if  src in p.text:
                Out_rcrd.append(r)

    # JobProperty = InputPins Record
    for r in job.findall(".//Property[@Name='InputPins']/.."):
        # Record{ Property StageType = src
        for p in r.findall(".//Property[@Name='StageType']"):
            if src in p.text:
                In_rcrd.append(r)
    
    return Out_rcrd,In_rcrd
    
def Subrecord_extract(Out_rcrd,In_rcrd):
    Out_sbrcrd = []
    In_sbrcrd = []

    # Out_rcrd Name = ValueSubrecord
    for i in range(len(Out_rcrd)):
        for sr in Out_rcrd[i].findall(".//Property[@Name='Value']/.."):
            # Subrecord Property Name = XMLProperties
            for p in sr.findall(".//Property[@Name='Name']"):
                if 'XMLProperties' in p.text:
                    Out_sbrcrd.append(sr)
                    
    # In_rcrd Name = Value  Subrecord
    for i in range(len(In_rcrd)):
        for sr in In_rcrd[i].findall(".//Property[@Name='Value']/.."):
            # Subrecord Property Name = XMLProperties
            for p in sr.findall(".//Property[@Name='Name']"):
                if 'XMLProperties' in p.text:
                    In_sbrcrd.append(sr)
                    
    return Out_sbrcrd, In_sbrcrd
    
def Source_extract(find_pattern, out_sbrcrd, src1):
    # Source table
    Source = []
    # Stop words
    Stop = ['loadMsgs.out','Dcom.ibm','ccjdbc.jar','is.cc','shared.jar']

    for sr in out_sbrcrd:
        t = sr.find(".//Property[@Name='Value']").text

        # Find Source TABLE 
        source = find_pattern.findall(t)
        # DB String
        db = ''
        for s in source:
            # Store db string(suppose only have 1)
            if ('DB_INFO.' in s) and (('_NAME' in s) or ('_URL' in s) or ('_DBNAME' in s)):
                replace = ['DB_INFO.','_NAME', '_DBNAME', '_URL']
                for r in replace:
                    s = s.upper().replace(r, '')
                db = src1 + '/' + s
        if db == '':
            db = 'TD/TD'
        elif db == 'DB':
            db = 'DB2/CFHADW'
        
        for s in source:
            # Store dbtype + db account + Source TABLE
            if (s not in Stop) and ('DB_INFO.' not in s) and ('PS_PATH.' not in s):
                Source.append(db + '/' + s.upper())
    # Remove dups
    Source = sorted(list(dict.fromkeys(Source)))
    
    return Source
    
def Target_extract(find_pattern, in_sbrcrd, src2):
    # Target table
    Target = []
    # Stop words
    Stop = ['loadMsgs.out','Dcom.ibm','ccjdbc.jar','is.cc','shared.jar']
    
    for sr in in_sbrcrd:
        t = sr.find(".//Property[@Name='Value']").text

        # Find SAS CR Target TABLE 
        target = find_pattern.findall(t)
        # DB String
        db = ''
        for s in target:
            # Store db string(suppose only have 1)
            if ('DB_INFO.' in s) and (('_NAME' in s) or ('_URL' in s) or ('_DBNAME' in s)):
                replace = ['DB_INFO.','_NAME', '_DBNAME', '_URL']
                for r in replace:
                    s = s.upper().replace(r, '')
                db = src2 + '/' + s
        if db == '':
            db = 'TD/TD'
        elif db == 'DB2/DB':
            db = 'DB2/CFHADW'
                
        for s in target:
            # Store dbtype + db account + Target TABLE
            if (s not in Stop) and ('DB_INFO.' not in s) and ('PS_PATH.' not in s):
                Target.append(db + '/' + s.upper())
    # Remove dups
    Target = sorted(list(dict.fromkeys(Target)))
    
    return Target
    
# Source -> src = CustomOutput;
# Target -> src = CustomInput;
# txt -> ty = file 
# dataset -> ty = dataset
def txt_extract(job,ty = 'dataset', src = 'CustomOutput'):
    txt = []
    find_pattern = re.compile(r'\w+\.\w+')
    # Source dataset
    for sr in job.findall(".//Record[@Type='%s']/Collection/SubRecord"%(src)):
        t = sr.find(".//Property[@Name='Name']").text
        if t == ty:
            ds = sr.find(".//Property[@Name='Value']")
            ds_t = find_pattern.findall(ds.text.upper())
            for s in ds_t:
                if '.TXT' in s or '.DS' in s or '.REJ' in s:
                    txt.append(s)
            #txt.append(ds.text.split('/')[1])
    return txt
    
    
def Main(Job):
    Dict = {"Job":[],"Source":[] ,"Target":[]}
    
    # ALL Job
    if Job == '*':
        Job = ",".join(job_list_all)
        
    for job in Job.split(','):
        print('-------------------------%s----------------------'%job.strip())
        # Dig into job
        Job_i = root.find(".//Job[@Identifier='%s']"%job.strip())
        l_s = 0
        l_t = 0
        # td/ db2/ edb
        for src in [td, db2, edb]:
            print('-------------------------Start %s Searching----------------------'%src)
            Out, In = Record_extract(job = Job_i, src = src)
            Out2, In2 = Subrecord_extract(Out,In)
            if src == 'TeradataConnectorPX':
                Source = Source_extract(td_find_pattern,Out2, src1 = '')
                Target = Target_extract(td_find_pattern,In2, src2 = '')
            else:
                Source = Source_extract(edb_find_pattern,Out2, src1 = src.replace('ConnectorPX', '').replace('JDBC', 'EDB'))
                Target = Target_extract(edb_find_pattern,In2, src2 = src.replace('ConnectorPX', '').replace('JDBC', 'EDB'))
                
            # Append Source/ Target
            for x in Source:
                Dict["Source"].append(x)
                l_s += 1
            for y in Target:
                Dict["Target"].append(y)
                l_t += 1
                
        # ds/ txt
        for ty in [ds, txt, txt2]:
            print('-------------------------Start %s Searching----------------------'%ty)
            Source_txt = txt_extract(Job_i,ty = ty, src = 'CustomOutput')
            Target_txt = txt_extract(Job_i,ty = ty, src = 'CustomInput')
            
            # Append Source/ Target
            for x in Source_txt:
                Dict["Source"].append(x)
                l_s += 1
            for y in Target_txt:
                Dict["Target"].append(y)
                l_t += 1
                
        # Find Bigger length and add up shorter col
        if l_s > l_t:
            l = l_s
            m = l_s - l_t
            Dict["Target"] += m * ['']
        elif l_s < l_t:
            l = l_t
            m = l_t - l_s
            Dict["Source"] += m * ['']
        else:
            l = l_s
        # Append Job
        Dict["Job"] += l * [job]
    print('-------------------------Export Result----------------------')
    Result = pd.DataFrame.from_dict(Dict)
    Result
    Result.sort_values(by = ['Job', 'Source'], ascending = True)
    Result.to_csv('%s_Result_out.csv'%xml)
    return Result
    
# Run 
if __name__ == "__main__":  
    # Parameters
    # ET Tree
    xml = input('Please enter xml name: ')
    tree = ET.parse('%s.xml'%xml)
    root = tree.getroot() 
    
    # Dig into Sjob
    job_list_all = []
    job_list = root.findall(".//Job")
    for j in job_list:
        job_list_all.append(j.attrib.get('Identifier'))
    
    # Job List
    Job = input('')
    
    # Source dict
    td = 'TeradataConnectorPX'
    db2 = 'DB2ConnectorPX'
    edb = 'JDBCConnectorPX'
    ds = 'dataset'
    txt = 'file'
    txt2 = 'file\(20)'

    # Find patterns
    td_find_pattern = re.compile(r'DP_CXL_[A-Za-z\_]+\.\w+')
    edb_find_pattern = re.compile(r'[A-Za-z\_]+\.\w+')
    
    print('-------------------------Start Searching----------------------')
    # Run
    Main(Job = Job)
    print('-------------------------End Searching------------------------')
