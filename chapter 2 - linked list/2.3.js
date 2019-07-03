const Node = require('./node');
const n = new Node('a');
n.next = new Node('b');
n.next.next = new Node('c');
n.next.next.next = new Node('d');
n.next.next.next.next = new Node('e');
n.next.next.next.next.next = new Node('f');

function deleteNode(n) {
  if (n === null || n.next === null) {
    return false;
  }
  n.next = n.next.next;
  return true;
}
function printNodes(_node) {
  while (_node !== null) {
    console.log(_node.data);
    _node = _node.next;
  }
}
console.log(deleteNode(n.next.next));
printNodes(n);
console.log(deleteNode(n.next.next.next));
printNodes(n);
