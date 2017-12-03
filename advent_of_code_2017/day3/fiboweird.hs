import qualified Data.Map as Map

main :: IO ()
main = do
  putStrLn (show (adjacents (0, 0)))
  putStrLn (show (dimension 24))
  putStrLn ("part2: " ++ (show (successor 368078)))

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

successor :: Int -> Int
successor n = do
  let matrix = Map.fromList [((0, 0), 1)]
  do_successor matrix n 1

default0 :: Maybe Int -> Int
default0 maybe_int = maybe 0 id maybe_int

do_successor :: Map.Map (Int, Int) Int -> Int -> Int -> Int
do_successor matrix destination n = do
  let maybe_val_at_pos = Map.lookup (pos n) matrix
  let val_at_pos = default0 maybe_val_at_pos
  if val_at_pos > destination
    then val_at_pos
    else do
      let n' = n + 1
      let adjacent_pos = adjacents (pos n')
      let elements = [Map.lookup x matrix | x <- adjacent_pos]
      let elem_values = [default0 x | x <- elements]
      let new_elem = sum elem_values
      let matrix' = Map.insert (pos n') new_elem matrix
      do_successor matrix' destination n'

adjacents :: (Int, Int) -> [(Int, Int)]
adjacents (a, b) = [(x, y) | x <- [a - 1, a, a + 1], y <- [b - 1, b, b + 1]]
