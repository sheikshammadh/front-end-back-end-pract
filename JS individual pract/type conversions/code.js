//implicit to string: it concats the strong and value
var result='123'+7;
console.log(result)
//=================================================================================
//implicit to number:it takes both strings as numbers
var result='5'-'5';
console.log(result)//0

var result='5'-'10'
console.log(result)//-5


var result='5'/'10'
console.log(result)//0.5

var result='5'*'10'
console.log(result)//50
//=====================================================================================
//implicit boolean to number: uses true=1 and all numbers as 1except 0, and false=0
var result='10'-true;
console.log(result)//9 true value is 1 so it remobed 1 from 10

var result='5'*'5'+false;
console.log(result)//25 false value is 0 so it is not added

var result='5'*'5'+true;
console.log(result)//26 true value is 1 so ir added 1 to 25
//==============================================================================================
var result='510';
console.log(result);
result=Number(result);
console.log(typeof(result))
//============================================================
var result="12345";
console.log(result);12345
result=Number(result);
console.log(typeof(result));//number
var str=String(result);
console.log(str);12345
console.log(typeof(str));//string

var result="12345";
console.log(result);12345
result=Boolean(result);//Boolean
console.log(typeof(result));
var str=Boolean(result);true
console.log(str);
console.log(typeof(str));//Boolean

var result="-12345";
console.log(result);//-12345
result=Boolean(result);
console.log(typeof(result));Boolean
var str=Boolean(result);
console.log(str);true
console.log(typeof(str));Boolean

var result=0;
console.log(result);0
result=Boolean(result);Boolean
console.log(typeof(result));
var str=Boolean(result);
console.log(str);false
console.log(typeof(str));Boolean
var a=134.124;
console.log(typeof(a));Number
console.log(parseInt(a));

var a=134.124;
console.log(typeof(a));
console.log(parseInt(a));
b=parseInt(a);
console.log(b);134

var a="134.124";
console.log(typeof(a)); String
console.log(parseInt(a));
b=parseInt(a);
console.log(b);134

var a=1;
console.log(String(a));//1
console.log(typeof(a))//number

var a="1";
console.log(String(a));//1
console.log(typeof(a))//string

var a="1";
console.log(Boolean(a));//true
console.log(typeof(a));//string