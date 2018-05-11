fn main() {
    println!("Hello, world!");

    println!("the sum is: {}", another_function(27, 2));

}

fn another_function(x: i32, y: i32) -> i32 {
    println!("The value of x and y are: {} and {}", x, y);
    x + y
}
