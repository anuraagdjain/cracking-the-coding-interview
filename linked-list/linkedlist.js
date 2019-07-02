'use strict';
const Node = require('./node');
class LinkedList {
  constructor() {
    this.head = null;
  }
  add(value) {
    const node = new Node(value);
    if (this.head) {
      node.next = this.head;
    }
    this.head = node;
  }
  delete(value = null) {
    /**
     * if `value` given delete that, else delete the first node.
     */
    if (value) {
      let curr = this.head,
        prev = null;
      while (curr != null) {
        if (curr.data === value) {
          prev.next = curr.next;
          curr = null;
          break;
        }
        prev = curr;
        curr = curr.next;
      }
    } else {
      this.head = this.head.next;
    }
  }
  listNodes() {
    let node = this.head;
    while (node != null) {
      console.log(node.data);
      node = node.next;
    }
  }
  /**
   * @description Allowing to iterate on the list.
   * @example
   * const a = new LinkedList();
   * a.add(1);
   * a.add(2);
   * a.add(3);
   * for(let n in a){
   * console.log(n);
   * }
   */
  *[Symbol.iterator]() {
    let node = this.head;
    while (node !== null) {
      yield node.data;
      node = node.next;
    }
  }
}

/**
 * Example
 */
// let list = new LinkedList();
// list.add(100);
// list.add(200);
// list.add(300);
// list.add(400);
// list.delete(200);
// console.log('After deleting 200');
// list.listNodes();
// console.log('\nAfter deleting first node');
// list.delete();
// list.listNodes();

module.exports = LinkedList;
