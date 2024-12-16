#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x))
{
    console.log('Missing number of occurences');
}
else
{
    let i = 0;
    while (i < x)
    {
        const text = 'C is fun'
        console.log(text);
        i++;
    }
}
