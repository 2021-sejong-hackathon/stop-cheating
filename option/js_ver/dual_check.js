// 1. child-process모듈의 spawn 취득
const spawn1 = require('child_process').spawn;

// 2. spawn을 통해 "python 파이썬파일.py" 명령어 실행 
const result1 = spawn('python', ['../python_ver/dual_check.py']);

// 3. stdout의 'data'이벤트리스너로 실행결과를 받는다. 
result1.stdout.on('data', function(data) {
    console.log(data.toString());
});

// 4. 에러 발생 시, stderr의 'data'이벤트리스너로 실행결과를 받는다. 
result1.stderr.on('data', function(data) { console.log(data.toString());
});