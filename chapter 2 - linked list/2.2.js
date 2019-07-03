const LinkedList = require('./linkedlist');
const list = new LinkedList();
// generate fake data
for (let i = 50; i >= 0; i--) {
  list.add(i);
}

let p1 = list.head,
  p2 = list.head;

for (let i = 0; i <= 8; i++) {
  if (p1 === null) process.exit(0);
  p1 = p1.next;
}
while (p1 !== null) {
  p1 = p1.next;
  p2 = p2.next;
}
console.log(p2);
