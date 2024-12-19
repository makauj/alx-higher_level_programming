#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if ((w < 1 && Number.isInteger(w)) || h < 0 && Number.isInteger(h)) {
            this.height = h;
            this.width = w;
        } else {
            return {};
        }
    }
    print() {
        if (w && h) {
            for (let i = 0; i < h; i++) {
                console.log('X'.repeat(w));
            }  
        }
    }
}
