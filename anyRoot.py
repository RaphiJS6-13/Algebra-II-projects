from decimal import Decimal
import re
def times(reps, callback):
	for _ in range(reps):
		callback()
def toSub(number):
	iter1 = list(str(number))
	out = ""
	for i in iter1:
		out += chr(8320 + int(i))
	return out

def c(i):
	if re.search(r"^\s*\d+(\.\d+)?\s*\$", i):
		return i
	elif re.search(r"\d+(\.\d+)?\s+\d+(\.\d+)?", i):
		print("\033[31m=>: SyntaxError: use `operand \033[3m*\033[23m operand` instead of `operand operand`\033[0m")
		return
	else:
		if re.search("[^\\(\\)\\%\\+\\-\\*\\/\\^\\d\\s\\.]+", i) or "$" in i:
			print(f"\033[31m=>: Syntax Error in calc: `" + re.search("[^\\s\\d]*[^\\(\\)\\%\\+\\-\\*\\/\\^\\d\\s\\.]+[^\\s\\d]*", i)[0] + "`;\033[0m")
			return
		ops = ["%", "^", "*", "/", "+", "-"]
		for op in ops:
			while op in i:
				print(i)
				try:
					num = r"\d+(\.\d+)?"
					match = re.search(f"{num}\\s*\\{op}\\s*{num}", i)[0]
				except TypeError:
					print("\033[31m=>: SyntaxError: bad or missing operands.\033[0m")
					return
				match1 = re.split(f"\\{op}", match)
				a = Decimal(match1[0])
				b = Decimal(match1[1])
				if op == "+": result = Decimal(a) + Decimal(b)
				if op == "-": result = Decimal(a) - Decimal(b)
				if op == "*": result = Decimal(a) * Decimal(b)
				if op == "/": result = Decimal(a) / Decimal(b)
				if op == "^": result = Decimal(a) ** Decimal(b)
				if op == "%": result = Decimal(a) % Decimal(b)
				i = re.sub(f"{num}\\s*\\{op}\\s*{num}", str(result), i)
		return i
class Repl:
	def __init__(self):
		self.calc = False
	def recur(self):
		base = input("What's your base?\n=>:")
		if base.strip() == "use calc":
			e = self.calc
			self.calc = True
			print("\033[38;2;0;255;0m=>: Calculation mode on.\033[0m")
			if e == True:
				print("\033[38;2;255;255;0m=>: Note:\n\tCalculation mode was already on.\033[0m")
			self.recur()
		elif base.strip() == "do not use calc" or base.strip() == "don't use calc":
			e = self.calc
			print("\033[38;2;0;255;0m=>: Calculation mode off.\033[0m")
			self.calc = False

			if e == False:
				print("\033[38;2;255;255;0m=>: Note:\n\tCalculation mode was already off.\033[0m")
			self.recur()
		elif base.strip() == "help":
			print("""
when the computer says `What's your base?...`:
	advanced commands:

		 1. help
			prints instructions

		 2. use calc 
			turns calculation mode on. 
			this supports the operators +, -, *, /, ^, and
			% (remainder of the quotient of 2 numbers),
			It does not support grouping (parentheses) yet.

		 3. don't use calc / do not use calc
			turns calc mode off.
	""")
			self.recur()
		elif not(re.search(r"^\d+(\.\d+)?$", base.strip()) or self.calc):
			print(f"\033[31m=>: Error: `{base}` is not a number.\033[0m")
			self.recur()
		elif base.strip() == "":
			self.recur()
		elif base.strip() == "0" or base.strip() == "0.0":
			print(f"\nresult: \033[1m(0)\033[0m\n")
			self.recur()
		else:
			t = c(base)
			if t == None:
				t = '0'
				self.recur()
				return
			elif t == "0" or t == "0.0":
				print(f"\nresult: \033[1m(0)\033[0m\n")
				self.recur()
				return
			if "$" in base:
				print("\033[31m=>: SyntaxError: $.\033[0m")
				self.recur()
			print("\u001b[1m^"+ t + "\u221a\u0304x\u0304\u001b[0m")
			base = Decimal(t)
			num = input("=>: What's your x?:")
			if not(re.search(r"^\d+(\.\d+)?$", num.strip()) or self.calc):
				print(f"\033[31m=>: Error: `{num}` is not a number.\033[0m")
				self.recur()
			elif num.strip() == "":
				self.recur()
			else:
				t = c(num)
				if t == None:
					t = '0'
					self.recur()
				num = Decimal(t)
				add = -Decimal(str(len(str(base)) - 1))
				output = Decimal("0")
				while len(str(output - int(output))) < 20:
					if output ** base == num:
						break
					while output ** base <= num:
						output += Decimal('10') ** -add
					output -= Decimal("10") ** -add
					add += 1
				print(f"\nresult: \033[1m({output})\033[0m")
				print(f"\n\033[2m({output} ^ {base} = {output ** base})\033[0m\n")
				self.recur()
print("""
/**
 * (c) 2019 @Raphael Spoerri
 *
 * version 0.2
 * 
 * type \033[3m`help`\033[0m for help
 * 
 * finds the `x` root of `y`.
 *
 * have fun!
 */
""")
w = Repl()
w.recur()
