const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(""));

const T = Number(input[0][0]);


function checkTestCase(num) {
    let arr = new Array();
    const l = num.length;


    for (let j = 0; j < l - 2; j++) {
        const p = num[j];
        const cIdx = j + 1;

        for (let w = cIdx + 1; w < l; w++) {
            console.log('continue 멈춤?', cIdx, w)
            if (num[cIdx] < num[w]) {
                arr.push(p);
                console.log('그대로 넣었다', arr, num[cIdx], num[w], p)
                break;
            } else if (num[cIdx] === num[w]){
                let sArr = num.slice(w, l);

                let cnt = sArr.filter(el => num[w] === el).length;
                if (cnt >= 2) {
                    arr.push(p);
                    console.log('값이 똑같은 거 있는데 그대로 넣었다', arr, num[cIdx], num[w], p)
                    break;
                }
            } else if (w === l - 1) {
                console.log('큰 수가 없음')
                let tArr = num.slice(j, w + 1);
                console.log('tArr : ', tArr, j, w)
                
                tArr = tArr.sort(function(a, b) {
                    if (a > b) return 1;
                    if (a === b) return 0;
                    if (a < b) return -1;
                });

                console.log('오름차순으로 정리한 tArr', tArr)
                
                for (let q = 0; q < tArr.length; q++) {
                    if (p < tArr[q]) {
                        arr.push(tArr[q]);
                        tArr.splice(q, 1);
                        break;
                    } else if (q === tArr.length - 1 && p >= tArr[q]) {
                        return 'BIGGEST'
                    }
                };
                console.log('가장 작은 수 넣은 뒤 ', arr, tArr)
                
                for (let h = 0; h < tArr.length; h++) {
                    arr.push(tArr[h]);
                };

                console.log('완성', arr)
                return arr;
            };
        };

    };

    if (num[l - 1] > num[l - 2]) {
        arr.push(num[l - 1]);
        arr.push(num[l - 2]);

        return arr
    } else {
        return 'BIGGEST'
    }
};

let answer = "";

for (let i = 1; i <= T; i++) {
    const tempAnwer = checkTestCase(input[i]);

    if (tempAnwer === 'BIGGEST') {
        answer += tempAnwer + "\n";
    } else {
        const tempL = tempAnwer.length;
        let temp = "";
        for (let i = 0; i < tempL; i++) {
            temp += tempAnwer[i];
        };
        answer += temp + "\n";
    };
};

console.log(answer)