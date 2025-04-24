const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    "/dev/stdin" : path.join(__dirname, 'input.txt')
).toString().trim()


let s = 0;
let i = 0;
const c = ['c=', 'c-', 'dz', 'd-', 'lj', 'nj', 's=', 'z='];
const l = input.length
while (i < l - 1) {
    const t = input[i] + input[i+1];
    if (c.includes(t)) {
        if (t === 'dz' && input[i+2] === '=') {
            s += 1;
            i += 3;

        } else if (t !== 'dz') {
            s += 1;
            i += 2;
        } else {
            s += 1;
            i += 1;
        }
    } else {
        s += 1;
        i += 1;
    }
};

if (i === l - 1) {
    s += 1;
};

console.log(s)