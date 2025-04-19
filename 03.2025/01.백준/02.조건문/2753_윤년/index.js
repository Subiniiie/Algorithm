const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();

if (input % 4 === 0) {
    if (input % 100 !== 0) {
        console.log(1);
    } else {
        if (input % 400 === 0) {
            console.log(1);
        } else {
            console.log(0);
        }
    }
} else {
    console.log(0);
}