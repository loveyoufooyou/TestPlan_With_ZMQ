# TestPlan with ZMQ

The project is a demo to simulate. Some devices need sockets to communicate with other controller. If you need to run tests in devices, can write down your `test_plan.csv` and write down the asynic function in `functions.py`. The UI is a simple html based on flask.

##  Framework chart
![图片](./static/picture.png)

## Run
We only run the web.py and `main.py`.

![图片](./static/web.png)

But before we do that, you could need to write down names of functions in the `test_plan.csv`.

Click the 'test' to run test, you can click 'stop' button to stop running program of tests.

## Why?
- The web.py and main.py are separated, because console and hardware are separated.
- Using ZMQ, because of selection of communication between hardware and other devices.
