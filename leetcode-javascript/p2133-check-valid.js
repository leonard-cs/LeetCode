/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var checkValid = function (matrix) {
    // check rows
    let n = matrix.length
    for (let i = 0; i < n; i++) {
        let set = new Set();
        for (let j = 0; j < n; j++) {
            let val = matrix[i][j];
            if (val < 1 || val > n || set.has(val)) return false;

            set.add(val);
        }
    }

    // check cols
    for (let i = 0; i < n; i++) {
        let set = new Set();
        for (let j = 0; j < n; j++) {
            let val = matrix[j][i];
            if (val < 1 || val > n || set.has(val)) return false;

            set.add(val);
        }
    }

    return true;
};

console.log(checkValid([[1, 2], [3, 4]]));