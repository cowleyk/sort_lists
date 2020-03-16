FROM python:3

# python function to sort list has rwx permissions for only the owner
# add a new group/user to keep permissions at rx for container user
RUN groupadd -r appuser && useradd -r -s /bin/false -g appuser appuser

WORKDIR /usr/src/app

COPY sort_lists.py ./

USER appuser

ENTRYPOINT ["python", "sort_lists.py"]
