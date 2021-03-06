﻿using System;
using NUnit.Framework;

namespace Razorvine.Serpent.Test
{

[TestFixture]
public class SlowPerformanceTest {

	// tests some performance regressions when they occur

	[Test]
	[Ignore("number parse performance in long lists has been resolved")]
	public void TestManyFloats()
	{
		const int amount = 200000;
		double[] array = new double[amount];
		for(int i=0; i<amount; ++i)
			array[i] = 12345.987654;
		
		Serializer serpent = new Serializer();
		Parser parser = new Parser();
		DateTime start = DateTime.Now;
		byte[] data = serpent.Serialize(array);
		double duration = (DateTime.Now - start).TotalMilliseconds;
		Console.WriteLine(""+duration+"  datalen="+data.Length);
		start = DateTime.Now;
		object[] values = (object[]) parser.Parse(data).GetData();
		duration = (DateTime.Now - start).TotalMilliseconds;
		Console.WriteLine(""+duration+"  valuelen="+values.Length);
	}

	[Test]
	[Ignore("number parse performance in long lists has been resolved")]
	public void TestManyInts()
	{
		const int amount=200000;
		int[] array = new int[amount];
		for(int i=0; i<amount; ++i)
			array[i] = 12345;
		
		Serializer serpent = new Serializer();
		Parser parser = new Parser();
		DateTime start = DateTime.Now;
		byte[] data = serpent.Serialize(array);
		double duration = (DateTime.Now - start).TotalMilliseconds;
		Console.WriteLine(""+duration+"  datalen="+data.Length);
		start = DateTime.Now;
		object[] values = (object[]) parser.Parse(data).GetData();
		duration = (DateTime.Now - start).TotalMilliseconds;
		Console.WriteLine(""+duration+"  valuelen="+values.Length);
	}	
}
}
