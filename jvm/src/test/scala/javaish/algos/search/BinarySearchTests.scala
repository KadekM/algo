package javaish.algos.search

import org.scalatest._
import org.scalatest.prop._
import org.scalacheck._

import javaish.algos.search._

class BinarySearchTests extends FlatSpec with Matchers {

  "empty array" should "return -1" in {
    BinarySearch.search(5, new Array[Int](0)) shouldBe -1
  }

  "[7] -> 7" should "find on index 0" in {
    BinarySearch.search(7, List(7).toArray) shouldBe 0
  }

  "[7] -> 145" should "not find" in {
    BinarySearch.search(145, List(7).toArray) shouldBe -1
  }

  "[1, 2, 3] -> 1" should "find on index 0" in {
    BinarySearch.search(1, List(1,2,3).toArray) shouldBe 0
  }

  "[1, 2, 3] -> 2" should "find on index 1" in {
    BinarySearch.search(2, List(1,2,3).toArray) shouldBe 1
  }

  "[1, 2, 3] -> 3" should "find on index 2" in {
    BinarySearch.search(3, List(1,2,3).toArray) shouldBe 2
  }
}

class BinarySearchProps extends PropSpec with PropertyChecks with Matchers {

  val nonEmptyArray = Gen.nonEmptyListOf(Arbitrary.arbInt.arbitrary)

  property("element from array is always found") {
    forAll(nonEmptyArray) { xs =>
      val arr = xs.toArray
      scala.util.Sorting.quickSort(arr)
      forAll(Gen.choose(0, arr.length-1)) { idx =>
        val foundOn = BinarySearch.search(arr(idx), arr)
        // dont compare indexes, because for repeating elements they may not be same [1, 2, 2, 3], which 2?
        arr(foundOn) shouldBe arr(idx)
      }
    }
  }

  property("empty array always return -1") {
    val emptyArr = List.empty[Int].toArray
    forAll { (idx: Int) =>
      BinarySearch.search(idx, emptyArr) shouldBe -1
    }
  }
}
