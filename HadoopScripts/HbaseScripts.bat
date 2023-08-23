create 'employees',  {NAME=> 'private'}, {NAME=> 'public'} 
put 'employees', 'ID1', 'private:ssn', '111-222-334'
put 'employees', 'ID2', 'private:ssn', '222-338-446'
put 'employees', 'ID3', 'private:address', '123  State St.'
put 'employees', 'ID1', 'private:address', '243 N. Wabash Av.'
scan 'employees'
put 'employees', 'ID1', 'private:firstname', 'Ronaldlee'
put 'employees', 'ID1', 'private:lastname', 'Ejalu'
put 'employees', 'ID1', 'private:age', '35'


put 'employees', 'ID2', 'private:firstname', 'Stevens'
put 'employees', 'ID2', 'private:lastname', 'Smith'
put 'employees', 'ID2', 'private:age', '46'

put 'employees', 'ID1', 'public:residentialstatus', 'Yes'
put 'employees', 'ID2', 'public:residentialstatus', 'Yes'

disable 'employees'
alter 'employees', 'department details'
enable 'employees'

put 'employees', 'ID1', 'department details:deptname', 'Data Services'
put 'employees', 'ID1', 'department details:deptno', 'HF001'

put 'employees', 'ID2', 'department details:deptname ', 'HR Services'
put 'employees', 'ID2', 'department details:deptno', 'HF100'
