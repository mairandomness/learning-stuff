main :: IO ()
main = do
  putStrLn (show (dimension 24))
  putStrLn ("part1: " ++ (show (distance 368078)))

elm :: (Int, Int) -> Int
elm (row, col) = do
  let max_rowcol = max (abs row) (abs col)
  let dim = max_rowcol * 2 + 1
  if row == -max_rowcol
    then dim ^ 2 - (max_rowcol - col)
    else if col == -max_rowcol
           then dim ^ 2 - dim + 1 - (max_rowcol + row)
           else if row == max_rowcol
                  then dim ^ 2 - 2 * dim + 2 - (max_rowcol + col)
                  else dim ^ 2 - 3 * dim + 3 - (max_rowcol - row)

dimension :: Int -> Int
dimension n = head ([2 * m + 1 | m <- [1 ..], n <= (2 * m + 1) ^ 2])

pos :: Int -> (Int, Int)
pos idx = do
  let dim = dimension idx
  let max_rowcol = div (dim - 1) 2
  let bottom_left = dim ^ 2 - dim + 1
  let top_left = dim ^ 2 - 2 * dim + 2
  let top_right = dim ^ 2 - 3 * dim + 3
  if idx >= bottom_left
    then (-max_rowcol, max_rowcol - (dim ^ 2 - idx))
    else if idx >= top_left
           then (-max_rowcol + (bottom_left - idx), -max_rowcol)
           else if idx >= top_right
                  then (max_rowcol, -max_rowcol + (top_left - idx))
                  else (max_rowcol - (top_right - idx), max_rowcol)

distance :: Int -> Int
distance n = do
  let (a, b) = pos n
  abs a + abs b
