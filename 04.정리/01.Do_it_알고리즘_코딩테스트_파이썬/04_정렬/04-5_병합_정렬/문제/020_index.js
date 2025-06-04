// 백준 2751

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, '020_input.txt')
).toString().trim().split("\n").map((el) => el.trim()).map(Number);

const N = input[0];
let A = new Array(N+1).fill(0);
let tmp = new Array(N+1).fill(0);

function mergeSort(s, e) {
    if (e - s < 1) {
        return
    };
    // 범위가 점점 줄어듦듦
    const m = Math.floor(s + (e - s) / 2)
    mergeSort(s, m)
    mergeSort(m+1, e)
    for (let i = s; i < e+1; i++) {
        tmp[i] = A[i];
    };

    let k = s;
    let index1 = s;
    let index2 = m + 1;

    // 두 그룹을 병합하는 로직직
    while (index1 <= m && index2 <= e) {
        if (tmp[index1] > tmp[index2]) {
            A[k] = tmp[index2];
            k += 1;
            index2 += 1;
        } else {
            A[k] = tmp[index1]
            k += 1;
            index1 += 1;
        }
    };

    // 한쪽 그룹이 모두 선택된 후 남아 있는 값 정리
    while (index1 <= m) {
        A[k] = tmp[index1]
        k += 1;
        index1 += 1;
    };
    while (index2 <= e) {
        A[k] = tmp[index2]
        k += 1;
        index2 += 1;
    };
};


for (let i = 1; i <= N; i++) {
    A[i] = input[i]; 
};

mergeSort(1, N)

let answer = "";

for (let i = 1; i <= N; i++) {
    answer += A[i] + "\n"
};

console.log(answer)