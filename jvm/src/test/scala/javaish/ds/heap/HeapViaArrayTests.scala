package javaish.ds.heap

import org.scalatest._
import org.scalatest.prop._
import org.scalacheck._

import javaish.ds.heap._

class HeapViaArrayTests extends PropSpec with PropertyChecks with Matchers  {


  property("2n and 2n+1 elem must be smaller than parent") {
    forAll(Gen.nonEmptyListOf(Arbitrary.arbInt.arbitrary)) { (xs: List[Int]) =>

      val heap = new HeapViaArray()
      for (x <- xs) { heap.insert(x) }
      val elems = heap.elems()

      forAll { (parentIdx: Int) =>
        whenever(parentIdx >= 0 && parentIdx < elems.length) {
          val leftIdx = 2 * parentIdx
          val rightIdx = 2 * parentIdx + 1


          if (leftIdx < elems.length)
            elems(parentIdx) should be >= elems(leftIdx)

          if (rightIdx < elems.length)
            elems(parentIdx) should be >= elems(rightIdx)
        }
      }

    }

  }

}
