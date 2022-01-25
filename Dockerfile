FROM kbase/sdkbase2:python
MAINTAINER KBase Developer
# -----------------------------------------
# In this section, you can install any system dependencies required
# to run your App.  For instance, you could place an apt-get update or
# install line here, a git checkout to download code, or run any other
# installation scripts.

RUN apt-get update
#RUN apt-get upgrade -y
RUN mkdir -p /kb/module/work
WORKDIR /kb/module

# Python and R requirements
RUN conda update -n base -c defaults conda

RUN conda create -y -n syncom --channel=conda-forge --channel=ccb-sb  r-base=3.5.1 r-tidyverse r-foreach r-data.table \
   r-optparse r-ggsignif r-cowplot r-RColorBrewer r-ggcorrplot r-vegan r-ade4 r-plyr  r-inflection

COPY ./requirements.kb_sdk.txt /kb/module/requirements.kb_sdk.txt
RUN pip install -r requirements.kb_sdk.txt
RUN pip install pandas
# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
