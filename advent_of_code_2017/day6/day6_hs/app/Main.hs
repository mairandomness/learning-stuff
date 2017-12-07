module Main where

import Data.List
import Data.Maybe
import Data.Vector.Unboxed as Vector
import Debug.Trace

input :: [Int]
input = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]

-- input = [0, 2, 7, 0]
main :: IO ()
main = do
  let vectorList = [] :: [Vector Int]
  let vector = Vector.fromList input :: Vector Int
  -- putStrLn $ show $ redistribute vector 2 7
  let result = findLoop vector vectorList
  putStrLn $ show $ fst result
  putStrLn $ show $ (+ 1) $ fromJust $ snd result

findLoop :: Vector Int -> [Vector Int] -> (Int, Maybe Int)
findLoop vector vectorList = do
  let vectorList' = vector : vectorList
  let maxIdx = Vector.maxIndex vector
  let maxVal = vector ! maxIdx
  let vector' = redistribute vector maxIdx maxVal
  if vector' `Prelude.elem` vectorList'
    then (Prelude.length vectorList', Data.List.elemIndex vector' vectorList')
    else findLoop vector' vectorList'

redistribute :: Vector Int -> Int -> Int -> Vector Int
redistribute vector maxIdx maxVal = do
  let withMaxZero = vector // [(maxIdx, 0)]
  let splitsTuple = Vector.splitAt (maxIdx + 1) withMaxZero
  let normalized = Vector.concat [snd splitsTuple, fst splitsTuple]
  let quotient = div maxVal $ Vector.length vector
  let remainder = rem maxVal $ Vector.length vector
  let plusQuotient = Vector.map (+ quotient) normalized
  let plusRemainder =
        Vector.imap
          (\idx val ->
             if idx < remainder
               then val + 1
               else val)
          plusQuotient
  let denormaIdx = (Vector.length vector) - maxIdx - 1
  let denormalized = Vector.splitAt denormaIdx plusRemainder
  Vector.concat [snd denormalized, fst denormalized]
