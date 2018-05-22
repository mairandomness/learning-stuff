fn main() {
    let s = String::from("hello");

    takes_ownership(&s);

    let x = 5;

    makes_copy(5);

    println!("Here is the value of x, even though it was used before and not borrowed: {}", x);
    println!("can't print s without using a reference or returning the string with the funtion \"&\": {}", s);
}

fn takes_ownership(some_string: &String) {
    println!("your string: {}", some_string);
}

fn makes_copy(some_integer: i32) {
    println!("your integer: {}", some_integer);
}
