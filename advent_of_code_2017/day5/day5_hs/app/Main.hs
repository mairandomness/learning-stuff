module Main where

import Lib
import System.IO (isEOF)

main :: IO ()
main = do
  contents <- getContents
  let instructionStrings = lines contents
  let instructions = map read instructionStrings :: [Int]
  let upperBound = length instructions
  let instructionsExecuted = walk instructions 0 0 upperBound
  putStrLn $ show instructionsExecuted

walk :: [Int] -> Int -> Int -> Int -> Int
walk instructions position stepCount upperBound = do
  if position >= upperBound || position < 0
    then stepCount
    else do
      let jump = instructions !! position
      let offset =
            if jump >= 3
              then -1
              else 1
      let instructions' = replaceNth position (jump + offset) instructions
      let position' = jump + position
      walk instructions' position' (stepCount + 1) upperBound

replaceNth :: Int -> a -> [a] -> [a]
replaceNth n newVal (x:xs)
  | n == 0 = newVal : xs
  | otherwise = x : replaceNth (n - 1) newVal xs
