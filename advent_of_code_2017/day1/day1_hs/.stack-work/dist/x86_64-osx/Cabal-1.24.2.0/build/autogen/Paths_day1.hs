{-# LANGUAGE CPP #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -fno-warn-implicit-prelude #-}
module Paths_day1 (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/Users/juliano/git/advent_of_code/day1/.stack-work/install/x86_64-osx/lts-9.14/8.0.2/bin"
libdir     = "/Users/juliano/git/advent_of_code/day1/.stack-work/install/x86_64-osx/lts-9.14/8.0.2/lib/x86_64-osx-ghc-8.0.2/day1-0.1.0.0-LKLId9gWgcN8O7u7p6ZsBZ"
dynlibdir  = "/Users/juliano/git/advent_of_code/day1/.stack-work/install/x86_64-osx/lts-9.14/8.0.2/lib/x86_64-osx-ghc-8.0.2"
datadir    = "/Users/juliano/git/advent_of_code/day1/.stack-work/install/x86_64-osx/lts-9.14/8.0.2/share/x86_64-osx-ghc-8.0.2/day1-0.1.0.0"
libexecdir = "/Users/juliano/git/advent_of_code/day1/.stack-work/install/x86_64-osx/lts-9.14/8.0.2/libexec"
sysconfdir = "/Users/juliano/git/advent_of_code/day1/.stack-work/install/x86_64-osx/lts-9.14/8.0.2/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "day1_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "day1_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "day1_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "day1_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "day1_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "day1_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
