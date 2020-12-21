package lab6;
import java.util.*;
import java.io.*;
import java.lang.*;
final public class Amacon implements Serializable{
	public	static	final long serialVersionUID = 42L;
	transient private Database db;	
	transient private static Scanner sc;
	private HashMap<String, Customer> customerdb;


	public Amacon()
	{
		this.db= new Database();
		Amacon.sc= new Scanner(System.in);
		this.customerdb = new HashMap<String, Customer>();
	}

	public static void serialize(Amacon a1) throws IOException, ClassNotFoundException
	{
		ObjectOutputStream	out	=	null;
		try
		{
			out = new ObjectOutputStream(new FileOutputStream("OUT.txt"));
			out.writeObject(a1);
		}
		finally
		{
			if(out!=null)
				out.close();
		}
	}

	public static Amacon deserialize(Amacon a1) throws IOException, ClassNotFoundException
	{
		ObjectInputStream	in	=	null;
		try
		{
			in = new ObjectInputStream(new FileInputStream("OUT.txt"));
			a1 = (Amacon) in.readObject();
			return a1;
		}
		finally
		{
			if(in!=null)
				in.close();
		}
	}

	public static void deserializeDb(Amacon a1) throws IOException, ClassNotFoundException
	{
		ObjectInputStream	in	=	null;
		try
		{
			in = new ObjectInputStream(new FileInputStream("database.txt"));
			Database db = (Database) in.readObject();
			if(db!=null)
			{
				a1.db = db;
			}
			else
			{
				System.out.println("null");
			}

		}
		finally
		{
			if(in!=null)
				in.close();
		}
	}


	public static void serializeDb(Amacon a1) throws IOException, ClassNotFoundException
	{
		Database db = a1.db;
		ObjectOutputStream	out	=	null;
		try
		{
			out = new ObjectOutputStream(new FileOutputStream("database.txt"));
			out.writeObject(db);
		}
		finally
		{
			if(out!=null)
				out.close();
		}
	}

	public static void serializeCust(Customer c1) throws IOException, ClassNotFoundException
	{
		ObjectOutputStream	out	=	null;
		try
		{
			out = new ObjectOutputStream(new FileOutputStream(c1.getName()+ "out.txt"));
			out.writeObject(c1);
		}
		finally
		{
			if(out!=null)
				out.close();
		}
	}

	public static Customer deserializeCust(Customer c1) throws IOException, ClassNotFoundException
	{
		ObjectInputStream	in	=	null;
		try
		{
			in = new ObjectInputStream(new FileInputStream(c1.getName()+ "out.txt"));
			c1 = (Customer) in.readObject();
			return c1;
		}
		finally
		{
			if(in!=null)
				in.close();
		}
	}





	public static void main(String[] args) throws NotNewException, NotExistingException, insufficientUnitsException, insufficientFundsException,ClassNotFoundException, IOException {
		Amacon a1 = new Amacon();
		try
		{
			a1 = deserialize(a1);
			deserializeDb(a1);
		}
		catch(IOException e)
		{
			System.out.println("No old database found");
		}
		catch(ClassNotFoundException e)
		{
			System.out.println("Class not found");
		}
		boolean run = false;
		while(!run)
		{
			System.out.println("Enter 1 if you want to act as Administrator");
			System.out.println("Enter 2 if you want to act as Customer");
			System.out.println("Enter 3 if you want to exit Amacon");
			sc = new Scanner(System.in);
			boolean inp = false;
			int choice = 0;
			while(!inp)
			{
				try
				{
					choice = sc.nextInt();
					if(choice == 1 || choice == 2 || choice ==3)
					{
						inp = true;
					}
				}
				catch (InputMismatchException e)
				{
					System.out.println("Please enter a valid integer input between 1-3.");
					sc.next();
				}
			}
			if(choice == 1)
			{
				char c = 'a';
				if(a1.db==null)
				{
					System.out.println("yes");
				}
				Admin admin = new Admin(a1.db);
				boolean adm2 = false;
				while(!adm2)
				{
					boolean adm = false;
					while(!adm)
					{
						System.out.println("Enter a if you want to insert a product/category.");
						System.out.println("Enter b if you want to delete a product/category.");
						System.out.println("Enter c if you want to search a product.");
						System.out.println("Enter d if you want to modify a product.");
						System.out.println("Enter e if you want to exit as Administrator.");
						c = sc.next().charAt(0);
						if(c=='a' || c=='b' || c=='c' || c=='d' || c=='e')
						{
							adm = true;
						}
						else
						{
							System.out.println("Please enter a valid character between a-e.");
						}
					}
					if(c=='a')
					{
						try
						{
							admin.insert();
						}
						catch (NotNewException e)
						{
							System.out.println(e.getMessage());
						}
					}
					else if(c=='b')
					{
						try
						{
							admin.delete();
						}
						catch (NotExistingException e)
						{
							System.out.println(e.getMessage());	
						}
					}
					else if(c=='c')
					{
						try {
							admin.search();
						}
						catch(NotExistingException e)
						{
							System.out.println(e.getMessage());
						}
					}
					else if(c=='d')
					{
						admin.modify();
					}
					else
					{
						adm2 = true;
						//						serialize(a1);
						//						serializeDb(a1);
					}
				}
			}
			else if(choice == 2)
			{
				char c ='a';
				Customer cust;
				System.out.println("Enter username of customer");
				String name= sc.next();
				if(a1.customerdb.containsKey(name))
				{
					System.out.println("Welcome "+name);
					cust = a1.customerdb.get(name);
					try {
						cust = deserializeCust(cust);
						System.out.println("Enter your choice");
						System.out.println("1. Recover cart");
						System.out.println("2. Fresh cart");
						boolean choice1 = false;
						while(!choice1)
						{
							int a=1;
							try
							{
								a = sc.nextInt();
							}
							catch(InputMismatchException e)
							{
								System.out.println("Enter valid number");
								sc.next();
							}
							switch (a) {
							case 1:
								cust.getShoppingCart().setDb(a1.db);
								choice1= true;
								break;
							case 2:
								cust.getNewShoppingCart(a1.db);
								choice1= true;
								break;

							default:
								System.out.println("Enter valid number");
							}


						}

						System.out.println(cust);
					}
					catch(IOException e)
					{
						System.out.println("No old database found");
					}
					catch(ClassNotFoundException e)
					{
						System.out.println("Class not found");
					}
				}
				else
				{
					System.out.println("Welcome new user!");
					cust = new Customer(name,new Cart(a1.db));
					a1.customerdb.put(cust.getName(), cust);
				}
				boolean cust2 = false;
				while(!cust2)
				{
					boolean cust1 = false;
					while(!cust1)
					{
						System.out.println("Enter a if you want to add funds.");
						System.out.println("Enter b if you want to add a product to your cart.");
						System.out.println("Enter c if you want to check out.");
						System.out.println("Enter d if you want to exit as Customer.");
						c = sc.next().charAt(0);
						if(c=='a' || c=='b' || c=='c' || c=='d')
						{
							cust1 = true;
						}
						else
						{
							System.out.println("Please enter a valid character between a-d.");
						}
					}
					if(c=='a')
					{
						System.out.println("Enter funds to be added");
						cust.addFunds(sc.nextInt());
					}
					else if(c=='b')
					{
						System.out.println("Enter product to be added and the desired quantity separated by a single space");
						try
						{
							cust.addProduct(sc.next(), sc.nextInt());
						}
						catch(NotExistingException e)
						{
							System.out.println(e.getMessage());
						}
						catch(insufficientUnitsException e)
						{
							System.out.println(e.getMessage());
						}
					}
					else if(c=='c')
					{
						try
						{
							System.out.println("You are being checked out!");

							cust.CheckOut();
						}
						catch (insufficientUnitsException e)
						{
							System.out.println(e.getMessage());
						}

						catch(insufficientFundsException e)
						{
							System.out.println(e.getMessage());
						}
					}
					else
					{
						cust2 = true;
						try
						{serializeCust(cust);}
						catch(IOException e)
						{
							System.out.println("IOException raised");
						}
						catch(ClassNotFoundException e)
						{
							System.out.println("Class not found");
						}
					}
				}
			}
			else
			{
				System.out.println("Revenue earned.");
				System.out.println(a1.db.calcRevenue());
				run = true;
				try
				{
					serializeDb(a1);
					serialize(a1);
				}
				catch(IOException e)
				{
					System.out.println("IOException raised");
				}
				catch(ClassNotFoundException e)
				{
					System.out.println("Class not found");
				}
			}
		}
	}

	public Database getDb() {
		return db;
	}
	
	
}
