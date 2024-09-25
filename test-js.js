var value = 100;
var hello = "123";
var myObj = {
  value: 1,
  func1: function () {
    console.log(`func1's this.value: ${this.value}`);

    var func2 = function () {
      console.log(this);
      console.log(`func2's this.value ${this.hello}`);
    };
    func2();
  },
};

myObj.func1();
