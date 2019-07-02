const LinkedList = require('./linkedlist');
const Node = require('./node');
const list = new LinkedList();
list.add(1);
list.add(2);
list.add(10);
list.add(5);
list.add(8);
list.add(5);
list.add(3);
const partition = 3;
const lessVal = new LinkedList();
const moreVal = new LinkedList();
let ll = list.head;

while (ll !== null) {
  if (ll.data < partition && ll.data !== partition) {
    lessVal.add(ll.data);
  } else {
    moreVal.add(ll.data);
  }
  ll = ll.next;
}
ll = lessVal.head;
while (ll.next !== null) {
  ll = ll.next;
}

lessVal.listNodes();
console.log('\r\n\r\n');
moreVal.listNodes();

// TODO: To Merge into single LL.
