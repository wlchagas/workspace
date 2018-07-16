/* var vs let vs const */

/*
var => function scope (até o fim da função)
let => block scope (até o fim do proximo bloco ('}'))
const => constant (fica na altura do escopo)

recomenda usar o let pois considera mais amigável as mensagens
de erro

quer meeesmo que usa o let
*/

// hoisting
// declarações de var vão automaticamente para cima
// possível de cair em 'undefined'

function funcaoQualquer() {
	console.log(name);
	var name = "Wellington Chagas";

	if (true){
		var a = 123;
	}

	{
		let b = 555;
	}

	console.log(a);

	console.log(name);
}

funcaoQualquer();