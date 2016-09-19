# kafka-http-input
Create a logstash input based on http-plugin

#### What is it ?
 This example shows the usage of logstash-http-input plugin. An external port can be used to write data to logstash which can be further visualized using kibana.

#### Usage:
 1. Install docker.
 2. Install `docker-compose`

    ```bash
    sudo pip install docker-compose
    ```

 3. In root-directory of this project run the following command. This will build the current elk image, install the `logstash-http-input` plugin, copy the `http-input.conf` file in logstash's configurations.

    `docker-compose up -d --build`

    The `http-input.conf` file contains some default configurations for e.g.Remaining configs can be found from here : [source](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-http.html)

    ```yaml
    Port: 3332
    user: myuser
    password: mypassword
    ```   
4. In another terminal run `elastic_logger.py` to generate data.

    `python elastic_logger.py`

    This following line in the code is used to post data on logstash-http-input.

    ```python
    requests.post(
        url='http://localhost:3332',
        data=json.dumps(payload),
        headers=self.headers,
        auth=('myuser', 'mypassword'))
    ```
5. Navigate to `http://localhost:5601` to see the kibana interface and click on `Discover` tab. The data from the topic would be there.
