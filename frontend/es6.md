## Be Careful Where You Break Lines

```javascript

//BROKEN CODE
const unexpected = function() {
  let first
	second = 1; // turning into a global variable
  console.log(first);
  console.log(second); 
}
unexpected(); 
console.log(second);

// OUTPUT
undefined
1
1
```

```javascript
//BROKEN CODE
const compute = function(number) {
  if (number > 5) {
    return number
    	+2;
  }
  if (number > 2) {
    return
    	number * 2;
  }
}
console.log(compute(6));
console.log(compute(3));

// OUTPUT
8
undefined
```

## Use === Instead of ==

```javascript
//BROKEN CODE
const a = '1'; 
const b = 1; 
const c = '1.0';
console.log(a == b); 
console.log(b == c); 
console.log(a == c);

// the check variable == null will yield true if variable is null or undefined and may be used instead of variable === null || variable === undefined.

// OUTPUT
true
true
false
```

```javascript
const a = '1';
const b = 1; 
const c = '1.0';
console.log(a === b); 
console.log(b === c); 
console.log(a === c);

// OUTPUT
false
false
false
```

## Declare Before Use

```javascript
// BROKEN CODE
const oops = function() {
  haha = 2; // make haha a global variable
  console.log(haha);
};

oops();
console.log(haha);

// OUTPUT
2
2
```

```javascript
// BROKEN CODE
const outer = function() {
  for(i = 1; i <= 3; i++) { // the variable fell into global scope
		inner(); 
  }
};
const inner = function() {
  for(i = 1; i <= 5; i++) {
		console.log(i);
  }
};
outer();

// OUTPUT
1
2
3
4
5
```

## Apply the use strict Directive

```javascript
//BROKEN CODE
'use strict';
const oops = function() {
haha = 2;
console.log(haha); };
oops(); console.log(haha);

```

