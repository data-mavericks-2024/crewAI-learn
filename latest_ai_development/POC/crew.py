from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
#from latest_ai_development.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

@CrewBase
class POCCrew():
	"""POC crew"""

	@agent
	def sales_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['sales agent'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def refund_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['refund agent'],
			verbose=True
		)

	@task
	def sales_task(self) -> Task:
		return Task(
			config=self.tasks_config['sales_task'],
		)

	@task
	def refund_task(self) -> Task:
		return Task(
			config=self.tasks_config['refund_task'],
			#output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the POC crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)