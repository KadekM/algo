package javaish.ds.heap

import org.scalatest._
import org.scalatest.prop._
import org.scalacheck._

import javaish.ds.heap._

class HeapViaArraySpec extends PropSpec with PropertyChecks with Matchers {

  def heapFromList(xs: TraversableOnce[Int]): HeapViaArray = {
    val heap = new HeapViaArray()
    xs.foreach(heap.insert)
    heap
  }

  val genHeap = Gen.listOf(Arbitrary.arbInt.arbitrary).map(heapFromList)
  val genNonEmptyHeap = Gen.nonEmptyListOf(Arbitrary.arbInt.arbitrary).map(heapFromList)

  property("left and right elems must be smaller than parent") {
    forAll(genHeap) { heap =>
      val elems = heap.elems()

      forAll { (parentIdx: Int) =>
        //whenever(parentIdx >= 0 && parentIdx < elems.length) {
        if (parentIdx >= 0 && parentIdx < elems.length) {
          val leftIdx = 2 * parentIdx + 1
          val rightIdx = 2 * parentIdx + 2

          if (leftIdx < elems.length)
            elems(parentIdx) should be <= elems(leftIdx)

          if (rightIdx < elems.length)
            elems(parentIdx) should be <= elems(rightIdx)
        }
      }
    }
  }

  property("top must always return minimum") {
    forAll(genNonEmptyHeap) { heap =>
      heap.top shouldBe heap.elems().min
    }
  }

  property("pop returns minimum") {
    forAll(genNonEmptyHeap) { heap =>
      while (heap.elems().length >= 1) {
        println(s"heap.elems=${heap.elems().mkString(",")}")
        val before = heap.elems()
        val popped = heap.pop()
        popped shouldBe before.min
        println(s"$popped . after heap.elems=${heap.elems().mkString(",")}")
      }
    }
  }
}
