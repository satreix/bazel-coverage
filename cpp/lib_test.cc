#include "lib.h"
#include "gtest/gtest.h"

TEST(General, AddTest) {
  EXPECT_EQ(add(1, 4), 5);
}
