package excercises.elems_of_prog_interview

object Ex20_10notify extends App {

  def printThread(msg: String) =
    println(s"${Thread.currentThread.getId} : $msg")

  class Buffer() {
    val n = 10
    private val arr = Array.ofDim[String](n)
    private var readAt = 0
    private var insertAt = 1

    def hasNext: Boolean =
      readAt < insertAt

    def next(): String =
      if (!hasNext)
        throw new RuntimeException(
          "Shouldn't have read, buffer consumer ahead of producer")
      else {
        val r = arr(readAt % n)
        readAt += 1
        r
      }

    def canPut: Boolean = insertAt - readAt < n

    def put(x: String): Unit =
      if (!canPut)
        throw new RuntimeException(
          "Shouldn't have put, buffer producer overriding unread data")
      else {
        arr(insertAt % n) = x
        insertAt += 1
      }
  }

  class Producer(shared: Buffer) {
    val r = scala.util.Random

    def start() =
      new Thread() {
        override def run(): Unit = {
          while (true) {
            val inserted = shared.synchronized {
              if (shared.canPut) {
                val str = (1 to 8).map(_ => r.nextPrintableChar).mkString
                shared.put(str)
                printThread("Putting")
                shared.notify()
              } else {
                printThread("Can't put")
                shared.wait()
              }
            }
          }
        }
      }.start()
  }

  class Consumer(shared: Buffer) {
    val r = scala.util.Random

    def start() =
      new Thread() {
        override def run(): Unit = {
          while (true) {
            shared.synchronized {
              val consumed =
                if (shared.hasNext) {
                  val consumed = shared.next()
                  printThread(s"Consuming: $consumed")
                  shared.notify()
                } else {
                  printThread("Sleeping")
                  shared.wait()
                }
            }
          }
        }
      }.start()
  }

  val r = scala.util.Random

  val buffer = new Buffer()

  val producer = new Producer(buffer)
  val consumer = new Consumer(buffer)

  producer.start()
  consumer.start()

}
