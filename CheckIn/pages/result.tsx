import { useRouter } from 'next/router'; // 引入 useRouter 钩子函数
import Nav from './layout'; // 引入导航组件
import React from 'react'; // 引入 React

function ResultPage() {
    const router = useRouter(); // 使用 useRouter 钩子函数获取路由信息
    const { lottery_number, won } = router.query; // 从路由查询参数中获取 lottery_number 和 won

    // 将 lottery_number 转换为字符串，并将其填充到至少三位数，不足部分用零补齐
    const lotteryId = lottery_number ? String(lottery_number).padStart(3, '0') : '';
    // 将 lotteryId 拆分成单个字符数组
    const [d0, d1, d2] = lotteryId.split('');

    return (
        <div className='bg-MidAutumnBg h-screen flex flex-col items-center justify-center'> {/* 设置背景图和布局样式 */}
            <Nav /> {/* 显示导航组件 */}
            <div className="text-center">
                <h1 className="text-3xl font-medium text-orange-200 mt-12">Result</h1> {/* 显示标题 */}
                {lottery_number && ( // 如果有 lottery_number，则显示抽奖结果
                    <div>
                        <h2 className="text-2xl font-medium text-orange-200">Your lottery number is: {lottery_number}</h2> {/* 显示抽奖号码 */}
                        <div className="flex gap-3 justify-center">
                            {/* 分别显示抽奖号码的每一位数字 */}
                            <div className="font-mono text-9xl bg-slate-200 shadow-inner rounded p-2 text-center opacity-60">{d0}</div>
                            <div className="font-mono text-9xl bg-slate-200 shadow-inner rounded p-2 text-center opacity-60">{d1}</div>
                            <div className="font-mono text-9xl bg-slate-200 shadow-inner rounded p-2 text-center opacity-60">{d2}</div>
                        </div>
                        <h3 className="text-xl font-medium text-orange-200 mt-4">Won: {won}</h3> {/* 显示是否中奖 */}
                    </div>
                )}
                {!lottery_number && ( // 如果没有 lottery_number，则显示提示信息
                    <p className="text-2xl font-medium text-orange-200 mt-4">No lottery number available currently...</p>
                )}
            </div>
        </div>
    );
}

export default ResultPage; // 导出 ResultPage 组件
