package excercises.elems_of_prog_interview

object Ex20_10 extends App {
  import scala.concurrent.ExecutionContext.Implicits.global
  import scala.concurrent.Future

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

    def start() = new Thread() {
      override def run(): Unit = {
        while (true) {
          val inserted = shared.synchronized {
            if (shared.canPut) {
              val str = (1 to 8).map(_ => r.nextPrintableChar).mkString
              shared.put(str)
              printThread("Putting")
              true
            } else {
              printThread("Can't put")
              false
            }
          }
          if (!inserted) Thread.sleep(r.nextInt(300))
        }
      }
    }.start()
  }

  class Consumer(shared: Buffer) {
    val r = scala.util.Random

    def start() = new Thread() {
      override def run(): Unit = {
        while (true) {
          val consumed = shared.synchronized {
            if (shared.hasNext) {
              Some(shared.next())
            } else {
              None
            }
          }

          consumed match {
            case Some(x) =>
              printThread(s"Consuming: $x")
            case None =>
              printThread("Sleeping")
              Thread.sleep(r.nextInt(300))
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
