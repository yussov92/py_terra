import asyncio
import subprocess
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class Terraform:
    def __init__(self, directory:str):
        # working directory - the place where the .tf file is located
        self.dir = directory
        logging.info(f'{self.dir} working directory')

    async def _run(self, cmd:str):
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
    
        stdout, stderr = await proc.communicate()
        if stdout:
            return stdout.decode()
        if stderr:
            return stderr.decode()

    def init(self):
        try:
            logging.info('Initialize a working directory')
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(self._run(f'terraform init {self.dir}'))
        except Exception as e:
            return e

    def plan(self):
        try:
            logging.info('Сreate an execution plan')
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(self._run(f'terraform plan {self.dir}'))
        except Exception as e:
            return e
        

    def apply(self):
        try:
            logging.info('Applies the changes')
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(self._run(f'terraform apply -auto-approve {self.dir}'))
        except Exception as e:
            return e

    def destroy(self):
        try:
            logging.info('Destroy infrastructure')
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(self._run(f'terraform destroy -auto-approve {self.dir}'))
        except Exception as e:
            return e

    def output(self, frmt:str, resource=''):
        try:
            logging.info('Get infrastructure info')
            loop = asyncio.get_event_loop()
            if frmt == 'json':
                return loop.run_until_complete(self._run(f'terraform output -json {resource}'))
            if frmt == 'text':
                return loop.run_until_complete(self._run(f'terraform output {resource}'))
        except Exception as e:
            return e