/* Functions! */

/* ******** ES 5 ******** */
/* Named Function | Função com nome */
function soma1(x,y) {
	return x + y;
}

/* Anonymous function | Função anônima */
var soma2 = function(x,y) {
	return x + y;
}

/* ******** ES 6 ******** */
/* Arrow function */
const soma3 = (x,y) => {
	return x + y;
}

const soma4 = (x, y) => x + y; // 1 parametro nao precisa de ()

const array1 = [1, 2, 3, 4, 5].map(function(x) {
	return x * 10;	
})

const array2 = [1, 2, 3, 4, 5].map((x) => { 
	return x * 10;
})

const array3 = [1, 2, 3, 4, 5].map((x) => x * 10)

// console.log(soma1(10,5))
// console.log(soma2(10,5))
// console.log(soma3(10,5))
// console.log(soma4(10,5))
// console.log(array2)