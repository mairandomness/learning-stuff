fn main() {
    for number in 1..101 {
        match number {
            number if (number % 15 == 0) => println!("CracklePop"),
            number if (number % 3 == 0) => println!("Crackle"),
            number if (number % 5 == 0) => println!("Pop"),
            _ => println!("{}", number),
        }
    }
}
