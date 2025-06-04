// 백준 11004


const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, '019_input.txt')
).toString().trim().split('\n').map((el) => el.trim().split(' ').map(Number));


const N = input[0][0];
const K = input[0][1];
let A = input[1];

function quickSprt(S, E, K) {
    if (S < E) {
        pivot = partition(S, E);
        
        if (pivot === K) {
            return
        } else if (K < pivot) {
            quickSprt(S, pivot - 1, K)
        } else {
            quickSprt(pivot + 1, E, K)
        }
    }
};

function swap(i, j) {
    [A[i], A[j]] = [A[j], A[i]];
};

function partition(S, E) {
    if (S+1 === E) {
        swap(S, E);

        return E
    }

    let M = Math.floor(S+E);
    swap(S, M);

    let pivot = A[S];
    i = S + 1;
    j = E;

    while (i <= j) {
        while (pivot < A[j] && j > 0) {
            j -= 1;
        };
        while (pivot > A[i] && i < A.length - 1) {
            i += 1;
        };
        if (i <= j) {
            swap(i, j);
            i += 1;
            j -= 1;
        };
    };

    A[S] = A[j];
    A[j] = pivot;
    return j
};

quickSprt(0, N - 1, K - 1)
console.log(A[K-1])