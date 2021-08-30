## 映射和集合

### 映射

#### Map对象

一个Map对象就是一个简单的键值对映射集合，可以按照数据插入时的顺序遍历所有的元素。

```javascript
var sayings = new Map();
sayings.set('dog', 'woof');
sayings.set('cat', 'meow');
sayings.set('elephant', 'toot');
sayings.size; // 3
sayings.get('fox'); // undefined
sayings.has('bird'); // false
sayings.delete('dog');
sayings.has('dog'); // false

for (var [key, value] of sayings) {
  console.log(key + ' goes ' + value);
}
// "cat goes meow"
// "elephant goes toot"

sayings.clear();
sayings.size; // 0
```

#### Object和Map的比较

一般地，`Object`会被用于将字符串类型映射到数值。`Object`允许设置键值对、根据键获取值、删除键、检测某个键是否存在。而`Map`具有更多的优势。

- `Object`的键均为`Strings`类型，在`Map`里键可以是任意类型。
- 必须手动计算`Object`的尺寸，但是可以很容易地获取使用`Map`的尺寸。
- `Map`的遍历遵循元素的插入顺序。
- `Object`有原型，所以映射中有一些缺省的键。（可以用 `map = Object.create(null) 回避`）

这三条提示可以帮你决定用`Map`还是`Object`：

- 如果键在运行时才能知道，或者所有的键类型相同，所有的值类型相同，那就使用`Map`。
- 如果需要将原始值存储为键，则使用`Map`，因为`Object`将每个键视为字符串，不管它是一个数字值、布尔值还是任何其他原始值。
- 如果需要对个别元素进行操作，使用`Object`。

#### WeakMap对象

`WeakMap`对象也是键值对的集合。它的**键必须是对象类型**，值可以是任意类型。它的键被弱保持，也就是说，当其键所指对象没有其他地方引用的时候，它会被GC回收掉。`WeakMap`提供的接口与`Map`相同。

与`Map`对象不同的是，`WeakMap`的键是不可枚举的。不提供列出其键的方法。列表是否存在取决于垃圾回收器的状态，是不可预知的。

###  集合

#### Set对象

`Set`对象是一组值的集合，这些值是不重复的，可以按照添加顺序来遍历。

```javascript
var mySet = new Set();
mySet.add(1);
mySet.add("some text");
mySet.add("foo");

mySet.has(1); // true
mySet.delete("foo");
mySet.size; // 2

for (let item of mySet) console.log(item);
// 1
// "some text"
```

### `Array`和`Set`的对比

一般情况下，在JavaScript中使用数组来存储一组元素，而新的集合对象有这些优势：

- 数组中用于判断元素是否存在的`indexOf` 函数效率低下。
- `Set`对象允许根据值删除元素，而数组中必须使用基于下标的 splice 方法。
- 数组的`indexOf`方法无法找到`NaN`值。
- `Set`对象存储不重复的值，所以不需要手动处理包含重复值的情况。

### `WeakSet`对象

`WeakSet`对象是一组对象的集合。`WeakSet`中的对象不重复且不可枚举。

与`Set`主要区别有：

- `WeakSets`中的值必须是对象类型，不可以是别的类型
- `WeakSet`的“*weak*”指的是，对集合中的对象，如果不存在其他引用，那么该对象将可被垃圾回收。于是不存在一个当前可用对象组成的列表，所以`WeakSets`不可枚举

`WeakSet`的用例很有限，比如使用DOM元素作为键来追踪它们而不必担心内存泄漏。