const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim());

const T = Number(input[0]);
let answer = "";

function nextPermutation(num) {
    num = num.split('');

    let i = num.length - 2;

    while (i >= 0 && num[i] >= num[i+1]) {
        i--;
    };
    
    if (i === -1) return 'BIGGEST';

    let j = num.length - 1;

    while (num[j] <= num[i]) {
        j--;
    };

    [num[i], num[j]] = [num[j], num[i]];

    let left = i + 1, right = num.length - 1;
    while (left < right) {
        [num[left], num[right]] = [num[right], num[left]];
        left++;
        right--;
    };

    return num.join('');
};


for (let i = 1; i <= T; i++) {
    answer += nextPermutation(input[i]) + "\n";
};

console.log(answer)
