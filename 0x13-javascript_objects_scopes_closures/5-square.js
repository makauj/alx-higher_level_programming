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
        if (this.width && this.height) {
            for (let i = 0; i < this.height; i++) {
                console.log('X'.repeat(this.width));
            }  
        }
    }
    rotate() {
        if (this.width && this.height) {
            [this.width, this.height] = [this.height, this.width];
        }
    }
    double() {
        if (this.width && this.height) {
            this.width *= 2;
            this.height *= 2;
        }
    }
}

class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }
}