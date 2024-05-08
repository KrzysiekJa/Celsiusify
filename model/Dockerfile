FROM tensorflow/serving:latest

ENV MODEL_BASE_PATH=/models
ENV MODEL_VERSION=/1/
ENV MODEL_NAME=saved_model

RUN mkdir -p ${MODEL_BASE_PATH}${MODEL_VERSION}

COPY . ${MODEL_BASE_PATH}${MODEL_VERSION}

EXPOSE 8501

RUN echo '#!/bin/bash \n\n\
tensorflow_model_server --rest_api_port=8501 \
--model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH} \
"$@"' > /usr/bin/tf_serving_entrypoint.sh \
&& chmod +x /usr/bin/tf_serving_entrypoint.sh

ENTRYPOINT ["/usr/bin/tf_serving_entrypoint.sh"]
