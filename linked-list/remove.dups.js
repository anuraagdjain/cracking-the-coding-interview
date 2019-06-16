'use strict';
const LinkedList = require('./linkedlist');
let list = new LinkedList();
list.add(1);
list.add(3);
list.add(2);
list.add(9);
list.add(5);
list.add(3);
list.add(4);
list.add(2);
list.add(5);

function removeDups(list) {
  let current = list.head;
  let prev = null;
  const listSet = new Set();
  while (current.next !== null) {
    if (listSet.has(current.data)) {
      prev.next = current.next;
    } else {
      listSet.add(current.data);
      prev = current;
    }
    current = current.next;
  }
}

removeDups(list);
list.listNodes();
