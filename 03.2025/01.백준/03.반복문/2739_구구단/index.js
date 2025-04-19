const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ? 
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();

for (let i = 1; i < 10; i++) {
    console.log(input + ' * ' + i + ' = ' + input * i);
}