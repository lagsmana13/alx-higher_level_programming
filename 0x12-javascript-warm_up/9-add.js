#!/usr/bin/node
function add (c, d) {
  const e = c + d;
  console.log(e);
}

add(Number(process.argv[2]), Number(process.argv[3]));
