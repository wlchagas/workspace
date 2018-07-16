/* Spread operator (...) */
const unidades = [1, 2, 3];
const dezenas = [10, 20, 30];

const numeros = [...unidades, ...dezenas];
console.log(numeros)

const obj1 = {
	a: 123
};

const obj2 = {
	b: "Olá"
};

const obj3 = { ...obj1, ...obj2};
console.log(obj3);