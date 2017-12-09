module Main where

import Data.Map (Map, (!))
import qualified Data.Map as Map
import Data.Maybe
import Lib
import System.IO (isEOF)

main :: IO ()
main = do
  contents <- getContents
  let ctlines = map words $ lines contents
  let regs = Map.empty :: Map String Int
  let (regs', maxEver) = foldl execute (regs, 0) ctlines
  let maxVal = maximum $ Map.elems regs'
  putStrLn $ show maxVal
  putStrLn $ show maxEver

execute :: (Map String Int, Int) -> [String] -> (Map String Int, Int)
execute (regs, maxEver) line = do
  let r1:opname:v1str:_:r2:fname:v2str:[] = line
  let r1val = fromMaybe 0 $ Map.lookup r1 regs
  let r2val = fromMaybe 0 $ Map.lookup r2 regs
  let op = opsMap ! opname
  let f = funcMap ! fname
  let v1 = read v1str :: Int
  let v2 = read v2str :: Int
  if f r2val v2
    then do
      let r1val' = op r1val v1
      (Map.insert r1 r1val' regs, maximum [maxEver, r1val'])
    else (regs, maxEver)

funcs :: [(String, (Int -> Int -> Bool))]
funcs =
  [ ("==", (==))
  , ("!=", (/=))
  , (">=", (>=))
  , ("<=", (<=))
  , (">", (>))
  , ("<", (<))
  ]

funcMap :: Map String (Int -> Int -> Bool)
funcMap = Map.fromList funcs

ops :: [(String, (Int -> Int -> Int))]
ops = [("inc", (+)), ("dec", (-))]

opsMap :: Map String (Int -> Int -> Int)
opsMap = Map.fromList ops
